```json
{
  "id": "bf83a8e836954c77",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288754,
  "host_pid": "9e6742732c60:1",
  "hash": "7dd84041eb515836a4145796fa44a668f4fa70790a02df21596db2d4aea81005",
  "cid": "QmV17dd84041eb515836a4145796fa44a668f4fa7079",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288754,
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
      "evaluated_at": 1760288754
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
  "sig": "4afcecc20aa5d2468e554d907021e7411c32cc8ca15463fd4a2ed15d2f819537"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240263900
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 25750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285764, 'matching_hash': 'e5d68d31887f65d4'}}}