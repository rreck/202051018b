```json
{
  "id": "263f589e6aec347c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294080,
  "host_pid": "9e6742732c60:1",
  "hash": "1a2278515399595c06988b91de1e7713e3455778aad6a8d12c5713c795084035",
  "cid": "QmV11a2278515399595c06988b91de1e7713e3455778",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294080,
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
      "evaluated_at": 1760294080
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
  "sig": "21f977624286b38f032117c69897a644e4fdb2b9f97e798a8e93a7452d15abee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277826130
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 14466144, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285764, 'matching_hash': '6123129413abd06e'}}}