```json
{
  "id": "82a3223ee7e904bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293784,
  "host_pid": "9e6742732c60:1",
  "hash": "20b85122ea2e8d3b6cccec6ac0053c0971e2e18ddab28532b887bba6cc6fbeff",
  "cid": "QmV120b85122ea2e8d3b6cccec6ac0053c0971e2e18d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293784,
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
      "evaluated_at": 1760293784
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
  "sig": "614597f038d4a60c0cebb24f7cebc9a34e7131739f9a538e271aca7f4eefe2ba"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590909791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 21329775, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285765, 'matching_hash': 'dd7dbd0f0c1d6f0c'}}}