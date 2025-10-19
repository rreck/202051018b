```json
{
  "id": "7ef1d3ba5d0df052",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289827,
  "host_pid": "9e6742732c60:1",
  "hash": "026eeeeeb59964aef0d63687f373253a3f7b0ab18538cd2c5a0a4dedc3ed2143",
  "cid": "QmV1026eeeeeb59964aef0d63687f373253a3f7b0ab1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289827,
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
      "evaluated_at": 1760289827
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
  "sig": "808a57610744833a0d60db589e990848d293d0d25ee75550232555bc60db3f25"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154261308
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285763, 'matching_hash': 'f5aec8f7458ab0e7'}}}een': 1760285763, 'matching_hash': '79f1dacfe7837a08'}}}