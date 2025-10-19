```json
{
  "id": "94848a15a1f05eaf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286252,
  "host_pid": "9e6742732c60:1",
  "hash": "4280dc2e9dc921a7f234248249d0c76f0bf6f43a0ab5eccb21f70b03fa1ceb7e",
  "cid": "QmV14280dc2e9dc921a7f234248249d0c76f0bf6f43a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286252,
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
      "evaluated_at": 1760286252
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
  "sig": "409453103acd6682c4297f1cf13a7efcd618351d06947e01a3d9ec1bc113d716"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105151957108
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285765, 'matching_hash': 'c64e753eaec43197'}}}