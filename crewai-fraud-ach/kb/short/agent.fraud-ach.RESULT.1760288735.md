```json
{
  "id": "ecfd46356785a809",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288735,
  "host_pid": "9e6742732c60:1",
  "hash": "d4c3834dda09dbca035b095c1f160902252ad21bbc7e948427645f2928c0109c",
  "cid": "QmV1d4c3834dda09dbca035b095c1f160902252ad21b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288735,
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
      "evaluated_at": 1760288735
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
  "sig": "87136c4849c81315f6636fa23364fb25531c530461c50d25f7556771ace059b0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274979410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285765, 'matching_hash': '00a04409f00be8e6'}}}