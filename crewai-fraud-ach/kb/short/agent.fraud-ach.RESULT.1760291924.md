```json
{
  "id": "2d2cc8fa7b90a839",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291924,
  "host_pid": "9e6742732c60:1",
  "hash": "330364fd7bd8f04832ab1f9a3f15d01a53f689a78db126f97c513d90b8290575",
  "cid": "QmV1330364fd7bd8f04832ab1f9a3f15d01a53f689a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291924,
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
      "evaluated_at": 1760291924
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
  "sig": "1986641ae3bdc62698f0c192ced82adcd6ccaff9b4998dca13123c6f787c44a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592366893
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 56918604, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285764, 'matching_hash': '065c48a9e05564fe'}}}