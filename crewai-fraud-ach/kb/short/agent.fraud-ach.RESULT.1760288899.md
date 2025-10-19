```json
{
  "id": "423106f1855ad090",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288899,
  "host_pid": "9e6742732c60:1",
  "hash": "7e94cc2a2d661779f5830cc5d171886dc301c980c3047ac5ebc0bdb0b46da479",
  "cid": "QmV17e94cc2a2d661779f5830cc5d171886dc301c980",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288899,
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
      "evaluated_at": 1760288899
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
  "sig": "8f90bc161fc89c641a0dde431697aa804a20afc22583bdc640a1fb049a8958f8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032712851
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285765, 'matching_hash': 'f72222764ca627d0'}}}