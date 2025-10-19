```json
{
  "id": "81c3bc121dcde773",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294077,
  "host_pid": "9e6742732c60:1",
  "hash": "6fdb157ced6e66a18f22fa1c0501f1529dc7df6252d704e4abaacb3102bddb69",
  "cid": "QmV16fdb157ced6e66a18f22fa1c0501f1529dc7df62",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294077,
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
      "evaluated_at": 1760294077
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
  "sig": "dbb50cbf38c29130920e47ce12c9642e696bd7cef65bd96edd064069b8c6146e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591886558
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 72591057, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '37bcf4c9c4817870'}}}