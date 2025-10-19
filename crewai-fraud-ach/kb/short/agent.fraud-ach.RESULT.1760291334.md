```json
{
  "id": "dc940792d9b63a5d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291334,
  "host_pid": "9e6742732c60:1",
  "hash": "8ca934905ae1b0a796fa9c3e08082147879a1e8d62d80fb750757f6b1652cbdc",
  "cid": "QmV18ca934905ae1b0a796fa9c3e08082147879a1e8d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291334,
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
      "evaluated_at": 1760291334
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
  "sig": "8c69e52577e037e0a148d4837681acc8d423559e0cc9137561738f56387bebcb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022308418
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 14773596, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285765, 'matching_hash': 'f2b6499d63eb1b6e'}}}