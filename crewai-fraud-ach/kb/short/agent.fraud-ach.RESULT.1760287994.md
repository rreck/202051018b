```json
{
  "id": "ae1400b80af12f04",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287994,
  "host_pid": "9e6742732c60:1",
  "hash": "39dda69083647d87a0248ae96df12ddb05b29c1a1d233019b5784aa956ee35b6",
  "cid": "QmV139dda69083647d87a0248ae96df12ddb05b29c1a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287994,
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
      "evaluated_at": 1760287994
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
  "sig": "667ff8b0e8e1201d0816a5d8ab3f2757b4838cb8145059ef49fda8692d867518"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276148173
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 22332905, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285765, 'matching_hash': 'f15677eba424e05f'}}}