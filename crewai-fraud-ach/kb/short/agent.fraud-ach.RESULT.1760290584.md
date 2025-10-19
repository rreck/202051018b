```json
{
  "id": "1a45434622d3bd19",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290584,
  "host_pid": "9e6742732c60:1",
  "hash": "9567d3f003e7443fe2964d2a68983c78b2dd1ccd632ee1b7c50239745a33862b",
  "cid": "QmV19567d3f003e7443fe2964d2a68983c78b2dd1ccd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290584,
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
      "evaluated_at": 1760290584
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
  "sig": "3eb8d70f9ed6ebda860280ff9a997a1d4a5cba80d059149fac3008e94fb21a45"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462989366
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 21818566, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285764, 'matching_hash': 'd084a7a97c1fb0c3'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '164661952', 'validation_error': 'Invalid routing number checksum'}}}