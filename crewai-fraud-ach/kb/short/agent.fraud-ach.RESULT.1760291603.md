```json
{
  "id": "7e9599d272ae0146",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291603,
  "host_pid": "9e6742732c60:1",
  "hash": "52e033623e4bff77024544c2dd87610ecb4cd260ffba4971ab0d2a5422165674",
  "cid": "QmV152e033623e4bff77024544c2dd87610ecb4cd260",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291603,
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
      "evaluated_at": 1760291603
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
  "sig": "653fc8b6a2da078a5fc36191c0f5046e092faf7bd825d1d7618cc4a3c5f72261"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278947252
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 39254879, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': 'c008d048aedbdb99'}}}