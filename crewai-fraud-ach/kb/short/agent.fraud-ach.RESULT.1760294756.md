```json
{
  "id": "c1a4a5872a62ffdb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294756,
  "host_pid": "9e6742732c60:1",
  "hash": "5755423adddae7b21c26b451dcad8e36690c906f2c2c7320987ffab83b50e0ad",
  "cid": "QmV15755423adddae7b21c26b451dcad8e36690c906f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294756,
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
      "evaluated_at": 1760294756
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
  "sig": "52218f0e345eb1e4ba9512bcb16bdca5ad48a490c3a77ac01835dcb58e226560"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464121559
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 110725492, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '1ddc8562b5a9ecf0'}}}