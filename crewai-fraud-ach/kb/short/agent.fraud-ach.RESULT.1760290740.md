```json
{
  "id": "724bf51bf0e14db9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290740,
  "host_pid": "9e6742732c60:1",
  "hash": "3c629f106fa57cde466c29a942fd5b79efb550a2d6edda30dec9cd9c14e825c0",
  "cid": "QmV13c629f106fa57cde466c29a942fd5b79efb550a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290740,
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
      "evaluated_at": 1760290740
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
  "sig": "8da0e1b43e8c9cf1bf1286ea10229b1cf8d05d7a7910a2a7ae5f23675e00f63a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024763111
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 31742674, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285764, 'matching_hash': '9fa093ca4f14e7a1'}}}