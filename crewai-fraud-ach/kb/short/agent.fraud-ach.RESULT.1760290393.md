```json
{
  "id": "39b7f7b8f68af344",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290393,
  "host_pid": "9e6742732c60:1",
  "hash": "4ddae70075a86683e6e3f0c128bbf3d0f77cf5a501db3b036218406c0a8f3c34",
  "cid": "QmV14ddae70075a86683e6e3f0c128bbf3d0f77cf5a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290393,
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
      "evaluated_at": 1760290393
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
  "sig": "ac1f0f375dfdbeaa87133f977fcd8fd02a912edda99f7dc38e0708ea347b16a6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151773289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 73287438, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': '7b1e6accdb666d6e'}}}