```json
{
  "id": "a281aa9be281cd9d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288933,
  "host_pid": "9e6742732c60:1",
  "hash": "762cfeb36b0e48e5791a057cd5cab87bedc9a8b26f0f6918094bcfced7617d61",
  "cid": "QmV1762cfeb36b0e48e5791a057cd5cab87bedc9a8b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288933,
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
      "evaluated_at": 1760288933
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
  "sig": "70329674b703f1e75f3150cc4eaacc0000c44cd0d3b2299e00e79abf4af44cda"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243970709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285765, 'matching_hash': '886d04c9297a738f'}}}