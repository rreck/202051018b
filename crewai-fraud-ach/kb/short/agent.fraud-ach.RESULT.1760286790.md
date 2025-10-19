```json
{
  "id": "980e33e3dcb4a8d4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286790,
  "host_pid": "9e6742732c60:1",
  "hash": "4302515e5f6ea8d1e56b474a497ca678936555e38153cf610d0122fdb6a19f06",
  "cid": "QmV14302515e5f6ea8d1e56b474a497ca678936555e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286790,
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
      "evaluated_at": 1760286790
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
  "sig": "3902703e0cd24bcc547cf8b16f7526a41af1efdbd71df545c6ff56e6284329eb"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201469526930
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285764, 'matching_hash': 'b6b808f7611ea662'}}}