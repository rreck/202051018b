```json
{
  "id": "b20fc7c980c519d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287051,
  "host_pid": "9e6742732c60:1",
  "hash": "d2c9e94a01a14dbf1dc1834b9754b944e7bade187af3003fd10e43d37593cc49",
  "cid": "QmV1d2c9e94a01a14dbf1dc1834b9754b944e7bade18",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287051,
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
      "evaluated_at": 1760287051
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
  "sig": "a52166f1407338964486dcd894f3a66b348837d712ec389f68533c3b2166f11f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009593192253
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285765, 'matching_hash': '48443a801d96c8b3'}}}