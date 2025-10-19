```json
{
  "id": "89e3b1f853b94a3b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291718,
  "host_pid": "9e6742732c60:1",
  "hash": "362897f5b5a81726b8b120cf9f183ce76c5264756a4542ad8f750833b0939b57",
  "cid": "QmV1362897f5b5a81726b8b120cf9f183ce76c526475",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291718,
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
      "evaluated_at": 1760291718
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
  "sig": "797d386bab137af3884d87f2bbca3cada6772827e325dea520121473c9d373b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150658717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 60531468, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285765, 'matching_hash': 'c0bd022b5af03ee8'}}}