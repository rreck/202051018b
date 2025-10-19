```json
{
  "id": "f7d759bc07fc93e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290633,
  "host_pid": "9e6742732c60:1",
  "hash": "47cb7f027a8d4d954fb31921fea12bbdf8a9642e9ea68bec9c5a2cfb495a6d8c",
  "cid": "QmV147cb7f027a8d4d954fb31921fea12bbdf8a9642e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290633,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760290633
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "2444c542346aba9552df13c1af3977fb8471471febe95b72e74c644f3e296fa9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463568898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 46370885, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285764, 'matching_hash': '8016b691bce48ab1'}}}