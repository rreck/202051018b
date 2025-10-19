```json
{
  "id": "67168731f0d64238",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290014,
  "host_pid": "9e6742732c60:1",
  "hash": "b213e0f096cea1d65162ab9c4210fa8a4b62237286dd122a0a2984c7bc6dd350",
  "cid": "QmV1b213e0f096cea1d65162ab9c4210fa8a4b622372",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290014,
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
      "evaluated_at": 1760290014
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
  "sig": "7cf2f0a6fbf02bade207bc7be73f3e88534a731ee449cdd155463644a50fdab3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463621906
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 47000904, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285763, 'matching_hash': 'c1b23d91813533f7'}}}