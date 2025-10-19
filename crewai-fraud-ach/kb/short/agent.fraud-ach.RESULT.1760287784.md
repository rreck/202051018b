```json
{
  "id": "3ad282f73e5c3cab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287784,
  "host_pid": "9e6742732c60:1",
  "hash": "b8e4308ad7c93145f0a71d833fb6a0e2de98f9e24c75b041a3d292b7bf723e32",
  "cid": "QmV1b8e4308ad7c93145f0a71d833fb6a0e2de98f9e2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287784,
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
      "evaluated_at": 1760287784
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
  "sig": "bbfb1867afab7cdf504f23616c2fbd11c8df9b0159ae2871581615609737df39"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 026009590178584
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285763, 'matching_hash': 'edc4255e13a93cc1'}}}een': 1760285765, 'matching_hash': '5fa0c304c44ad0bf'}}}