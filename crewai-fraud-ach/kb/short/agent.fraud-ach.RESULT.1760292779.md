```json
{
  "id": "577cb7674b1e7321",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292779,
  "host_pid": "9e6742732c60:1",
  "hash": "b1ce35b2920055ca3c7344e0d0564805f81d0278b78bf8076df8dabd4f3e7d71",
  "cid": "QmV1b1ce35b2920055ca3c7344e0d0564805f81d0278",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292779,
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
      "evaluated_at": 1760292779
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
  "sig": "540142ad2403eebb4fe2619e916f09627281d79c51d23788cd6ec09e666d1cb9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152274101
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 36777615, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': 'b0ffab0948116893'}}}