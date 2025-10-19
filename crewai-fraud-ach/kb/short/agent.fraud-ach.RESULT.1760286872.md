```json
{
  "id": "a505d344b44016de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286872,
  "host_pid": "9e6742732c60:1",
  "hash": "2eeea4c2e495e780d2409e51b6b462566b4ba9f9631fc58ff24a93a75fab921d",
  "cid": "QmV12eeea4c2e495e780d2409e51b6b462566b4ba9f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286872,
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
      "evaluated_at": 1760286872
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
  "sig": "2dfbc198db860c87a1304c27d6264800144f2d2b278c1a864e7a405e7da22d8e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156872006
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285763, 'matching_hash': '001baa6337a96952'}}}