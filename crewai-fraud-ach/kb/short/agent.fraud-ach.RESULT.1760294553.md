```json
{
  "id": "b044c9f651ef2405",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294553,
  "host_pid": "9e6742732c60:1",
  "hash": "2c00225b994ee4260f485a2f75cd5abe4324c4061c79afc09c3d85c2184a6800",
  "cid": "QmV12c00225b994ee4260f485a2f75cd5abe4324c406",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294553,
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
      "evaluated_at": 1760294553
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
  "sig": "4207befcf810e64ec7edd47e212cbc06b8346bb6c7ef3951a10be1cb5973bd9b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152435370
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 38480640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': '79f1dacfe7837a08'}}}