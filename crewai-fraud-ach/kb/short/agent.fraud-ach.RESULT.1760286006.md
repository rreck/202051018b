```json
{
  "id": "e3a9e38aee6817f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286006,
  "host_pid": "9e6742732c60:1",
  "hash": "703235a6fbfa46aab72a9392b8fc1b4ccec2ca1e4acffc4dc11044ebc79bc6c4",
  "cid": "QmV1703235a6fbfa46aab72a9392b8fc1b4ccec2ca1e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286006,
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
      "evaluated_at": 1760286006
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
  "sig": "22141defe614da3462248be6ec11b5c013d095b59dfc518e22d091b01817fbb9"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000022841229
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285763, 'matching_hash': '5d206cfe266207b6'}}}