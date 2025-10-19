```json
{
  "id": "f074858e76f03fe1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291960,
  "host_pid": "9e6742732c60:1",
  "hash": "9d73537a274d65af5a839a9b18476ae28cb9c84b15866c761596199ceedb6312",
  "cid": "QmV19d73537a274d65af5a839a9b18476ae28cb9c84b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291960,
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
      "evaluated_at": 1760291960
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
  "sig": "e380c2a62e5ea4424049858a82e50ef1a8e75a8e10b5a32deb5a5a14739e560a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593654177
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 61417158, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285764, 'matching_hash': '5fbc310f1a1fe9dc'}}}