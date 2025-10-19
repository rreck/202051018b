```json
{
  "id": "abd7e629266b9a68",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293356,
  "host_pid": "9e6742732c60:1",
  "hash": "47ed568aa09603f4f83b66e306b1a19636a296b8313ee0660207ec64cce4d662",
  "cid": "QmV147ed568aa09603f4f83b66e306b1a19636a296b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293356,
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
      "evaluated_at": 1760293356
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
  "sig": "7f1ac923381fbfc058dd34a24af7c8e841ffbde3a04eb6710a5886af7f05b640"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025560621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 58945880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': '1e88fa5a655ec1c9'}}}