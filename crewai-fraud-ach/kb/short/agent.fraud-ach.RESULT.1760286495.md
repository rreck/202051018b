```json
{
  "id": "e6a23b20229247f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286495,
  "host_pid": "9e6742732c60:1",
  "hash": "1a82d866181fcffeffd4b5c8295d697c33e88eac74703431fdc2be8d50faf28b",
  "cid": "QmV11a82d866181fcffeffd4b5c8295d697c33e88eac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286495,
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
      "evaluated_at": 1760286495
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
  "sig": "c1d077a1f9974f06c6103ae81ea7347f7a22f259c7e2e7351a36ecf77db619fd"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241978752
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285765, 'matching_hash': '600b54b59692179b'}}}