```json
{
  "id": "2829dc264f328209",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294382,
  "host_pid": "9e6742732c60:1",
  "hash": "4b93ff34ce1c3bd5117ca4133f8b06dc827d8b4aef12dda9501b3867b626d375",
  "cid": "QmV14b93ff34ce1c3bd5117ca4133f8b06dc827d8b4a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294382,
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
      "evaluated_at": 1760294382
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
  "sig": "6884879f68af8fc0e731214712af94855e43aacaca235ea0063809bf74ebc2ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029303857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 61936158, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': '4510d576292a5401'}}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}