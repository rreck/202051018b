```json
{
  "id": "f886aee34785d9bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287575,
  "host_pid": "9e6742732c60:1",
  "hash": "f84419a23dcb79fa1d5eca6bea3c91803e99563e12cf01918761d120fef5a6cd",
  "cid": "QmV1f84419a23dcb79fa1d5eca6bea3c91803e99563e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287575,
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
      "evaluated_at": 1760287575
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
  "sig": "7a3901bfa7b131d0a7b096d7664f9861d361f9067bc0f0589ac0543bd84066b0"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 021000023603818
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 29186690, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285764, 'matching_hash': '07334b550f79eb68'}}}