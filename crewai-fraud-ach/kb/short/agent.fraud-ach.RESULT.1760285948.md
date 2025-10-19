```json
{
  "id": "39d6ef4a9ed7a33c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285948,
  "host_pid": "9e6742732c60:1",
  "hash": "757d58bf525ad94a44c425746abe5c0429ae968be344151a919b62efc27d9e93",
  "cid": "QmV1757d58bf525ad94a44c425746abe5c0429ae968b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285948,
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
      "evaluated_at": 1760285948
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
  "sig": "3d041e0b7dc2bba7003866db98ae99733fa4cc30f6107a53fad66efded63e04c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105155322765
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285763, 'matching_hash': '7a27d1bb592c5069'}}}