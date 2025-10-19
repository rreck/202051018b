```json
{
  "id": "e7384f9e6b6053e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293971,
  "host_pid": "9e6742732c60:1",
  "hash": "e5100830835520de9d48b60e8e240a305ac56a7d2e36165e756077ab06f13abe",
  "cid": "QmV1e5100830835520de9d48b60e8e240a305ac56a7d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293971,
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
      "evaluated_at": 1760293971
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
  "sig": "48f5ea145123910217f9a41ffb893b51e50b1417f7602c78b2ba4872116304cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596556765
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 42054476, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': '746e82f5d57aeb25'}}}