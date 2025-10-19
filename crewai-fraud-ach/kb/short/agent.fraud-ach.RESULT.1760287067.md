```json
{
  "id": "2077f53fbcde5960",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287067,
  "host_pid": "9e6742732c60:1",
  "hash": "613b8d0ee5f3d403ebe9be8e7aa1ac42e8e94249da80c0147d378f9bd6bf79d8",
  "cid": "QmV1613b8d0ee5f3d403ebe9be8e7aa1ac42e8e94249",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287067,
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
      "evaluated_at": 1760287067
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
  "sig": "bce0ee74787d7faf28abc9dc4e0a50571216142277aba1425753a8f309ec6f21"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009591602283
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285763, 'matching_hash': '995d19d96715feaf'}}}