```json
{
  "id": "d6a308707166f464",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293071,
  "host_pid": "9e6742732c60:1",
  "hash": "8289f812f876fce6261c67b74992f16718fbe4305e8e85bf942a078a510224d4",
  "cid": "QmV18289f812f876fce6261c67b74992f16718fbe430",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293071,
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
      "evaluated_at": 1760293071
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
  "sig": "bd35606eee473feecfbb934c06f2fb3965cbfd86d438c6c0d55624b624e2af71"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024298856
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 72012190, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': 'c651031c314af1fc'}}}