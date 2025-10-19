```json
{
  "id": "638e826b9a9917eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293380,
  "host_pid": "9e6742732c60:1",
  "hash": "bf8a092d7246b7dfd9d00b0b897001b051db07e6af33e2135e17dca088b61602",
  "cid": "QmV1bf8a092d7246b7dfd9d00b0b897001b051db07e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293380,
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
      "evaluated_at": 1760293380
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
  "sig": "d7288a74f898bd416a9bdb77e2343d26d61ed60334ef105029a821e7209fef1a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599017181
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 38451966, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': '7f94592234367703'}}}