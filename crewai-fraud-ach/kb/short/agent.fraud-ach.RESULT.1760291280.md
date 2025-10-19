```json
{
  "id": "18f2cc0a878af460",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291280,
  "host_pid": "9e6742732c60:1",
  "hash": "609f743a586649edd5c5c606d5f56d488b3aca8960ed6da503ad2cc491e15179",
  "cid": "QmV1609f743a586649edd5c5c606d5f56d488b3aca89",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291280,
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
      "evaluated_at": 1760291280
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
  "sig": "f4bca24368db8fa3172129dca0881114ba6fe5cfe2a545958869fe3735b691b1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278613406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 70454394, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285765, 'matching_hash': 'bc206509fe1a9621'}}}