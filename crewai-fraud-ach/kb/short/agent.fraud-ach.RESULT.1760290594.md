```json
{
  "id": "4db73e6e713680d3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290594,
  "host_pid": "9e6742732c60:1",
  "hash": "8808b1991d72199e03d2648557f94168600d4a7e8c86197de78864ebbcc23c0c",
  "cid": "QmV18808b1991d72199e03d2648557f94168600d4a7e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290594,
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
      "evaluated_at": 1760290594
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
  "sig": "efa96ededb25c636be3385b12f1efec108e0806284de2eac48659ab1b26159df"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593456245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 74193042, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285764, 'matching_hash': '5bbbd28055422217'}}}