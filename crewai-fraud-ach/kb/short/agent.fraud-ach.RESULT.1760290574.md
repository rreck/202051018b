```json
{
  "id": "e126b7775aeca630",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290574,
  "host_pid": "9e6742732c60:1",
  "hash": "35e6360fddb80ed106f8ce7d1ce31e50e8277e768ef72ca8e93dc23edc9272f8",
  "cid": "QmV135e6360fddb80ed106f8ce7d1ce31e50e8277e76",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290574,
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
      "evaluated_at": 1760290574
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
  "sig": "22998852528010aec60a6a6b5a25c413e9a6f955dea0f114c64da0a8d279fd37"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035823466
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 67245640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': 'b8896a43cee69b83'}}}