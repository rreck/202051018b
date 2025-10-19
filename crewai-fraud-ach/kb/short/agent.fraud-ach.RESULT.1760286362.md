```json
{
  "id": "587620e4707ccb6a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286362,
  "host_pid": "9e6742732c60:1",
  "hash": "8cdd3bfeb74c47951328c2e8c61236581903e11b00bdb5bfeeea4c7ae25fa3ed",
  "cid": "QmV18cdd3bfeb74c47951328c2e8c61236581903e11b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286362,
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
      "evaluated_at": 1760286362
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
  "sig": "9c27f0e179ec0eb282e7ef5a4de745c3c8286974c35cde616757c1172209bcb4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000024088542
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285763, 'matching_hash': '45759aa393537ed9'}}}