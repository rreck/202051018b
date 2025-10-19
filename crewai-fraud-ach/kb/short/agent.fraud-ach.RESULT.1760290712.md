```json
{
  "id": "22791d2794198a19",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290712,
  "host_pid": "9e6742732c60:1",
  "hash": "f0ad8b63eac8dbdb9c53b9f059859057ce563215a315ea479d4b56f5661b311b",
  "cid": "QmV1f0ad8b63eac8dbdb9c53b9f059859057ce563215",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290712,
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
      "evaluated_at": 1760290712
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
  "sig": "35bad2bd3de86323914f6aef8ed97ef55aea728746db38aa05e3294c51351e12"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020141329
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 74174650, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285764, 'matching_hash': '1e11ace6091d7a38'}}}