```json
{
  "id": "d00458ccd64fdbc2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290978,
  "host_pid": "9e6742732c60:1",
  "hash": "b6b52d8187b700e621caf9a48295bd53565169f81432a7ad6a6f2a7bae30c690",
  "cid": "QmV1b6b52d8187b700e621caf9a48295bd53565169f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290978,
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
      "evaluated_at": 1760290978
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
  "sig": "c4fb976f9de00c950b82b3cf0b17a5a40562c70600e4132cf027685156176a87"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020641018
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 26520768, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': '9cb08faa1a3d5c0e'}}}