```json
{
  "id": "b9753444d6dab776",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291831,
  "host_pid": "9e6742732c60:1",
  "hash": "2bd8fd3acd47eb4b95054516ec5b9bce327dbb2b3781da84e38b005c2b0f510f",
  "cid": "QmV12bd8fd3acd47eb4b95054516ec5b9bce327dbb2b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291831,
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
      "evaluated_at": 1760291831
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
  "sig": "514917a3f9cb41d4bdedd2fba03a7ff0f63ace296925d975adaf9044f38ac8fc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022136987
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 65434816, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': 'e25bac2e01df376b'}}}