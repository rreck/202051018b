```json
{
  "id": "d19896a7f5532935",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294825,
  "host_pid": "9e6742732c60:1",
  "hash": "7ad7a783d11d184c3f3bccf58ddd24de345e5c93904709543b89ebb3c948f185",
  "cid": "QmV17ad7a783d11d184c3f3bccf58ddd24de345e5c93",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294825,
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
      "evaluated_at": 1760294825
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
  "sig": "b2d828ebfddd153df3c94d1cc9df5422461907da5901675d3a30541051361486"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026682072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 82362875, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285764, 'matching_hash': 'ef2983ea6f6c1303'}}}}