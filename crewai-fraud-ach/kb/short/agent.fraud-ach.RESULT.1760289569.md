```json
{
  "id": "22a81a49042aa83a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289569,
  "host_pid": "9e6742732c60:1",
  "hash": "d47d804e3fc1010b3726b73dd9f93a116b1496c66a33c6541c59584d71573856",
  "cid": "QmV1d47d804e3fc1010b3726b73dd9f93a116b1496c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289569,
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
      "evaluated_at": 1760289569
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
  "sig": "abf77a6faef0aa975db278e0fc623a8a0e49be2c6d09ccf061c2f106ff997d13"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595770141
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 11481308, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285763, 'matching_hash': '07c751792fcc9457'}}}