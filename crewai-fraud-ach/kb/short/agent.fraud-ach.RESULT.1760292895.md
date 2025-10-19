```json
{
  "id": "742512a302d33852",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292895,
  "host_pid": "9e6742732c60:1",
  "hash": "90c08b574fa94590a0defe16932f5b69f082e77b8664dec32f79a733627ac413",
  "cid": "QmV190c08b574fa94590a0defe16932f5b69f082e77b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292895,
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
      "evaluated_at": 1760292895
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
  "sig": "887e2ba7485fd718d5f1ebdbe7645fcd436c05dd720984b0a23c2f71aecdb071"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594679703
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 18985626, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285765, 'matching_hash': 'e094f64527cf9b58'}}}