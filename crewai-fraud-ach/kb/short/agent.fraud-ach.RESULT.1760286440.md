```json
{
  "id": "a7d85074a580d91e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286440,
  "host_pid": "9e6742732c60:1",
  "hash": "c09b4cf5b915e00e39726aef5178efd472c7a67df15646e2898bc32d63ac6874",
  "cid": "QmV1c09b4cf5b915e00e39726aef5178efd472c7a67d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286440,
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
      "evaluated_at": 1760286440
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
  "sig": "ab0c3535c4691063edebe2f41f4a19fb3894313acb38c23295f094dd5860dce7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000244752813
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285765, 'matching_hash': 'eddee7b4753d10e9'}}}