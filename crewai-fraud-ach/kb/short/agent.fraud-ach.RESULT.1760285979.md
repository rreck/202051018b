```json
{
  "id": "8b172986f5dc0d6d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285979,
  "host_pid": "9e6742732c60:1",
  "hash": "e6aa475d36893c9f67e3d94c3efa6464bc4dff2f6f901f043ea215b677664b41",
  "cid": "QmV1e6aa475d36893c9f67e3d94c3efa6464bc4dff2f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285979,
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
      "evaluated_at": 1760285979
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
  "sig": "afa72f8948a34ceebb95ed20d4e2f700ade2f0b37a77b00a5587f22faeb78ce5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201469526930
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285764, 'matching_hash': 'b6b808f7611ea662'}}}