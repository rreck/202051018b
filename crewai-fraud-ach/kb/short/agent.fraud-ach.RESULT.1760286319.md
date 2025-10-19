```json
{
  "id": "3abb9860d074d3d6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286319,
  "host_pid": "9e6742732c60:1",
  "hash": "0e7b3e3e585ed8cee17617264df7e2a880a5733c0e9b8cf518bb34cf8456165c",
  "cid": "QmV10e7b3e3e585ed8cee17617264df7e2a880a5733c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286319,
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
      "evaluated_at": 1760286319
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
  "sig": "a43cdbc9ccbe5e02cf297d653d44fa04e305dfb64fe1aba20ae039cd5481b7c7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}