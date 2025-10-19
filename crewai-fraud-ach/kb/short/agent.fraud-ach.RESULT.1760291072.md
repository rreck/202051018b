```json
{
  "id": "e704852e3f85d2f7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291072,
  "host_pid": "9e6742732c60:1",
  "hash": "4aa068bf550bb11533d1a3c1bd738b3e88f4cd91629fd700b5440127ab693b14",
  "cid": "QmV14aa068bf550bb11533d1a3c1bd738b3e88f4cd91",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291072,
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
      "evaluated_at": 1760291072
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
  "sig": "3d9459c8cbea827725495812577046144b147c37d6a190e476f9265bf9b04625"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590178584
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 17495072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285763, 'matching_hash': 'edc4255e13a93cc1'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}