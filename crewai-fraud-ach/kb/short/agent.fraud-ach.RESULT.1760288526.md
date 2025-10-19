```json
{
  "id": "d6d35ffd0d7be3cc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288526,
  "host_pid": "9e6742732c60:1",
  "hash": "eb9bf17636b2fa9d164a04a981bb6aa0600f33b6ce5c1b1e4d76788063d22913",
  "cid": "QmV1eb9bf17636b2fa9d164a04a981bb6aa0600f33b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288526,
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
      "evaluated_at": 1760288527
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
  "sig": "d33a75b29e75f0c4a7916f7a32f0e6a94489960fbbe0d856379ed2dcb521b607"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247109361
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285763, 'matching_hash': '3efad933d2b7f9bd'}}}