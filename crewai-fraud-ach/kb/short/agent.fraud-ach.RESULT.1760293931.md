```json
{
  "id": "599ef94db98b15c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293931,
  "host_pid": "9e6742732c60:1",
  "hash": "c013196feb5daa368fba2c5dd36fbbbb553bc0785773240a99c44d26dbe16d40",
  "cid": "QmV1c013196feb5daa368fba2c5dd36fbbbb553bc078",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293931,
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
      "evaluated_at": 1760293931
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
  "sig": "a6f73eb42a9c0090936f71968711cfc0d846ef32789393feb03a60a790cdfef2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026783731
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 93807408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': 'dea6d8bb62de6c67'}}}