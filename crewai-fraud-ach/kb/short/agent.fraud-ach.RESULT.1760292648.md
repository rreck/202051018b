```json
{
  "id": "9ce53b82b14fee63",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292648,
  "host_pid": "9e6742732c60:1",
  "hash": "bd5981aa1ff657d709ac2422f149ed06b6d8c2393a5079ff8b4f27d596ba7967",
  "cid": "QmV1bd5981aa1ff657d709ac2422f149ed06b6d8c239",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292648,
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
      "evaluated_at": 1760292648
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
  "sig": "a1bff0ecfd9ce885fed8064161d3637b94b07adb8abd3403c86ca11763a2b777"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273021249
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 97413490, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285764, 'matching_hash': '8f9c0aaacb6951b9'}}}